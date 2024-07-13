After unzipping, keep the directory structure intact.

First, run "make" to compile the C++ solver.

Then run:
  python3 steinertree.py infile
where "infile" is the name of the input file in the "/instances" directory
but without the ".in" extension.

Example:
  python3 steinertree.py 6pin_ryan

This will read the instance from 6pin_ryan.in, display the solution, and save both
the plain text solution (6pin.sol) and the image (6pin.pdf) to the "/solutions" directory.

The input format is simple, look at /instances/6pin_ryan.in for an example if you want
to add your own instances.

NOTE
Unless you want to update constants in the C++ code, any instance you add should
have at most 20 points, all with x and y coordinates in the range [0,7].

If you do want to update constants, look at the comments at the top of the C++
code to understand the running time and memory use.

I haven't tested it with different grid sizes, so I don't know how the images will look
if you change the grid size.