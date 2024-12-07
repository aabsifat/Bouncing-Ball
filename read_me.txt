This program creates an animated simulation of balls moving and interacting within a defined space, adhering to a specific set of rules.
The animation models the motion of balls as they bounce off walls and interact with each other, following pre-defined physical behaviors.

Motion of the Balls:
Each ball moves in one of four fixed directions: Northeast (NE), Southeast (SE), Northwest (NW), or Southwest (SW).
Each iteration results in the ball moving ±x pixel horizontally and ±y pixel vertically.

Wall Interaction: Balls reflect off walls in a manner analogous to a mirror reflection.

Ball Interaction:
Head-On Collision - Balls reverse their directions upon impact.
Orthogonal Collision - Balls reflect as if hitting a mirror, keeping their shared directional components unchanged.
Parallel Movement - Balls moving in the same direction do not interact.

Design Guidelines and Assumptions:
Balls are generated fully inside the simulation window.
No two balls overlap at initialization.
All balls are uniform in size and velocity.