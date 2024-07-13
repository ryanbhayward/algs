/*
  Implementation of the Dreyfus-Wagner algorithm for Steiner tree but only for
  Rectilinear Steiner Tree inputs.

  Author: Zac Friggstad

  Reads input from stdin, prints solution to stdout.

  Input format:
  n_points
  x1 y1
  x2 y2
  ...

  The points must have coordinates lying in [0, 7] and the number of points can be at
  most 20. You can change these limits by updating the constants GSIZE and MAX_PTS
  near the top of the code, but keep in mind the running time and space usage below.

  Running time: O(g^2 * 3^k + g^4 * 2^k)
  Here g = square grid length (g = 8 by default) and k = the number of
  terminals in the input.

  Space usage: dominated by two tables of 16-bit integers of size 2^(MAX_PTS)*GSIZE*GSIZE
  each. At default values of MAX_PTS = 20 and GSIZE = 8 these take 2^29 bytes in total.
*/

#include <iostream>
#include <cassert>
#include <cmath>
#include <algorithm>

const int GSIZE = 8;
const int MAX_PTS = 20;

// VERY IMPORTANT THIS IS NOT CHANGED
// the code assumes INF is the all-1 bit pattern
const uint16_t INF = 0xffff;

// number of points, x/y coordinates of the given points
// and a mapping of grid points to their index in pts_x/y (or -1 if not a given point)
int n_pts;
int pts_x[GSIZE*GSIZE], pts_y[GSIZE*GSIZE];
int pt_index[GSIZE][GSIZE];

// read an instance from stdin, see comments at the start of this file
// for the input format
void read_points() {
  assert(std::cin >> n_pts);
  assert(1 <= n_pts && n_pts <= MAX_PTS);
  
  memset(pt_index, -1, sizeof(pt_index));

  for (int i = 0; i < n_pts; ++i) {
    // read the next point and make sure it is valid (in the grid and not already
    // given earlier in the input)
    int x, y;
    assert(std::cin >> x >> y);
    assert(0 <= x && x < GSIZE && 0 <= y && y < GSIZE);
    assert(pt_index[x][y] == -1);

    pts_x[i] = x;
    pts_y[i] = y;
    pt_index[x][y] = i;
  }
}

// DP tables
uint16_t memo_f[1<<MAX_PTS][GSIZE][GSIZE];
uint16_t memo_g[1<<MAX_PTS][GSIZE][GSIZE];

// forward declaration of g() function since f() and g() call each other
uint16_t g(int, int, int);

// f(Y, wx, wy) is the cheapest Steiner tree solution having terminals Y \cup {(wx,wy)}
// here Y represents a subset of given points as a bitset
// (i'th bit of Y is 1 iff the i'th input point is in the set)
uint16_t f(int Y, int wx, int wy) {
  uint16_t& ans = memo_f[Y][wx][wy];

  if (ans == INF) {
    int hw = __builtin_popcount(Y); // number of 1 bits in Y
    if (pt_index[wx][wy] == -1 || (Y&(1<<pt_index[wx][wy])) == 0) ++hw;
    // hw is now the number of points in Y \cup {(wx,wy)}

    if (hw == 1) {
      // only one terminal, nothing to do
      ans = 0;
    }
    else if (hw == 2) {
      // two terminals, one must be (wx,wy)
      // first we determine the other one
      int vx, vy;
      for (int i = 0; i < n_pts; ++i)
        if (Y&(1<<i) && i != pt_index[wx][wy]) {
          vx = pts_x[i];
          vy = pts_y[i];
        }
      // the solution is the Manhattan distance between these points
      ans = abs(wx-vx) + abs(wy-vy);
    }
    else {
      // otherwise try all other points (vx,vy) and call g()
      for (int vx = 0; vx < GSIZE; ++vx)
        for (int vy = 0; vy < GSIZE; ++vy)
          ans = std::min(ans, uint16_t(abs(wx-vx) + abs(wy-vy) + g(Y, vx, vy)));
    }
  }
  return ans;
}

// the auxiliary g function
// will try all non-trivial splits of Y into subsets Z,Y-Z
// and compute the cheapest Steiner tree solutions over terminals Z \cup {(vx,vy)}
// and (Y-Z) cup {(vx,vy)}
uint16_t g(int Y, int vx, int vy) {
  uint16_t& ans = memo_g[Y][vx][vy];
  if (ans == INF) {
  // this nifty loop has Z iterate through all subsets of Y
  // in the bitset representation of the sets
  // i.e. it will count up from Z to Y but only along those bits that are subsets of Y
    for (int Z = 0; Z < Y; Z = ((Z|~Y)+1)&Y)
      if (Z) ans = std::min(ans, uint16_t(f(Z, vx, vy) + f(Y^Z, vx, vy)));
  }
  return ans;
}

// print all line segments connecting (x1,y1) to (x2,y2)
// along a minimum-length path (Manhattan distance)
void print_path(int x1, int y1, int x2, int y2) {
  if (x1 > x2) {
    std::swap(x1, x2);
    std::swap(y1, y2);
  }

  while (x1 < x2) {
    std::cout << x1 << ' ' << y1 << ' ' << x1+1 << ' ' << y1 << '\n';
    ++x1;
  }

  if (y1 > y2) std::swap(y1, y2);

  while (y1 < y2) {
    std::cout << x1 << ' ' << y1 << ' ' << x1 << ' ' << y1+1 << '\n';
    ++y1;
  }
}

// prints the line segments in the optimal solution to the Steiner tree instance
// with terminals Y \cup {(wx, wy)} to standard output in the format
// sx1 sy1 ex1 ey1 (the start and end coordinates of a length-1 line segment)
// sx2 sy2 ex2 ey2
// ...
void print_sol(int Y, int wx, int wy) {
  int hw = __builtin_popcount(Y); // number of 1 bits in Y
  if (pt_index[wx][wy] == -1 || (Y&(1<<pt_index[wx][wy])) == 0) ++hw;

  // do the same calculations as f() except instead of trying all recursive calls
  // we just find which one yielded the same value as f() and do that one
  if (hw == 1) return;
  if (hw == 2) {
    int vx, vy;
    for (int i = 0; i < n_pts; ++i)
      if (Y&(1<<i) && i != pt_index[wx][wy]) {
        vx = pts_x[i];
        vy = pts_y[i];
      }
    print_path(wx, wy, vx, vy);
    return;
  }

  // if we get here, there are at least three terminals
  // try all vx,vy and see which one gave the same value as f(Y,v)

  for (int vx = 0; vx < GSIZE; ++vx)
    for (int vy = 0; vy < GSIZE; ++vy)
      if (f(Y, wx, wy) == abs(wx-vx) + abs(wy-vy) + g(Y, vx, vy)) {
        // we found a match! the optimal solution for subproblem (Y,wx,wy)
        // used wx,wy
        print_path(wx, wy, vx, vy);
        // now try all splits of Y as in g(Y,vx,vy) to see which one leads to the optimal solution
        for (int Z = 0; Z < Y; Z = ((Z|~Y)+1)&Y)
          if (Z > 0 && g(Y, vx, vy) == f(Z, vx, vy) + f(Y^Z, vx, vy)) {
            // Z is the correct split of Y in the optimal solution so
            // we recursively print the optimal solutions after this split
            print_sol(Z, vx, vy);
            print_sol(Y^Z, vx, vy);
            return;
          }

      }
    
}

int main(int argc, char** argv) {
  read_points();
  memset(memo_f, INF, sizeof(memo_f));
  memset(memo_g, INF, sizeof(memo_g));

  // // first print the points in the input (for the plotting function)
  // std::cout << n_pts << '\n';
  // for (int i = 0; i < n_pts; ++i) std::cout << pts_x[i] << ' ' << pts_y[i] << '\n';

  int X = (1<<n_pts)-1;
  // print the optimal solution cost, which is also the same as the number of
  // length-1 line segments that will be printed next
  std::cout << f(X, pts_x[0], pts_y[0]) << '\n';

  print_sol(X, pts_x[0], pts_y[0]);

  return 0;
}