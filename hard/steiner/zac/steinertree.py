import matplotlib.pyplot as plt
import sys, os, time

GSIZE = 8

if __name__ == "__main__":
  if len(sys.argv) != 2:
    print("Usage: python3 steinertree.py filename (no extension)")
    print("Example: python3 steinertree.py 6pin")
    print("Reads input from instances/6pin.in and stores solution in solutions/6pin.ans and image in solutions/6pin.pdf")
    print("Also requires solve_st.cpp to be copiled to an executable named solve_st in the same directory.")
    sys.exit(1)

  in_file = "instances/{0}.in".format(sys.argv[1])
  sol_file = "solutions/{0}.ans".format(sys.argv[1])
  pdf_file = "solutions/{0}.pdf".format(sys.argv[1])


  # read the input from the input file
  with open(in_file, "r") as input_file:
    pts = [tuple(map(int, input_file.readline().split())) for _ in range(int(input_file.readline()))]
  
  # display the input file contents
  print(in_file,"contains",len(pts),"pins:")
  for p in pts: print("  - ", p)

  # call the C++ program to solve the instance
  print()
  print("Now solving...")
  cmd = "./solve_st < {0} > {1}".format(in_file, sol_file)
  start_time = time.time()
  os.system(cmd)
  end_time = time.time()
  print("Done in {0:.04f} seconds (wall clock)".format(end_time - start_time))
  
  # read the solution from the solution file
  with open(sol_file, "r") as solution_file:
    sol = [tuple(map(int, solution_file.readline().split())) for _ in range(int(solution_file.readline()))]

  # display the solution and save to a file
  print()
  print("Solution cost:", len(sol))
  print("Solution:")
  for x1,y1,x2,y2 in sol:
    print("  -", (x1,y1), (x2,y2))
  print("Saving solution to", sol_file)

  # the rest of this script is for generating the solution image

  print()
  print("Generating .pdf and saving to", pdf_file)

  # physical size of the plot
  plt.rcParams["figure.figsize"] = (10, 10)
  plt.axis("off")

  # print a label underneath
  txt = "{0} : {1} pins : solution cost {2}".format(sys.argv[1]+".in", len(pts), len(sol))
  plt.figtext(0.5, 0.08, txt, wrap=True, horizontalalignment='center', fontsize=24)

  # draw the given pins as dots
  for x,y in pts:
    plt.plot(x,y,'o',color="black",markersize=15)

  # plots a line segment, making it thicker if it is in the solution
  def plot_seg(seg):
    if seg in sol: lw = 5
    else: lw = 0.5
    plt.plot((seg[0], seg[2]), (seg[1], seg[3]), color="black", linewidth = lw)

  # plot all line segments
  for x in range(GSIZE):
    for y in range(GSIZE):
      if x+1 < GSIZE: plot_seg((x,y,x+1,y))
      if y+1 < GSIZE: plot_seg((x,y,x,y+1))
  
  # finally save to the pdf file and display
  # comment out plt.show() if you don't want it to open a
  # window displaying the solution when running this script
  plt.savefig(pdf_file)
  plt.show()
