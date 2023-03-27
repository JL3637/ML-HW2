# Homework 2
1. (d)<br>
2. (b)<br>
   Prove: There is two upper bound for d_vc, one is depend on the dimension of x which is d_vc <= 6210 + 1, and the other one is depend on the number of perceptrons, since one perceptron can implement one dichotomy, we can use 2^N <= 1126 to find out d_vc <= lg(1126). And it is obvious that d_vc <= lg(1126) is a tighter bound.
3. (e)<br>
   Prove:<br>
   (a) d_vc = 4, since for N = 5, we can't implement {1, -1, 1, -1, 1} this dichotomy.<br>
   (b) d_vc = 4, since mh(5) < 2^5, because {1, -1, 1, -1, 1} and {-1, 1, -1, 1, -1} are both not dichotomies.<br>
   (c) d_vc = infinity, since sin is a oscillation function by putting N points between (-1, 1) properly we can implement 2^N dichotomies by changing different w.<br>
   (d) <br>
   (e) <br>
4. ()<br>
5. (b)<br>
   • some set of d distinct inputs is shattered by H
   • any set of d + 1 distinct inputs is not shattered by H
