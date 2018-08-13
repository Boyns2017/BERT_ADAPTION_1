// Agent robot in project Reactive_BDI_Env.mas2j

/* Initial beliefs and rules */

/* Initial goals */

!setup.

/* Plans */
                                                    
+!setup : meta <- .print("Robot is activated") !activate.
+!setup : true <- !setup.


+!activate : leg1 <- -meta[source(meta)]; !dropped.
+!activate : leg2 <- -meta[source(meta)]; !dropped.
+!activate : leg3 <- -meta[source(meta)]; !dropped.
+!activate : leg4 <- -meta[source(meta)]; !dropped.

+!dropped : robot_does_not_notice <- -meta[source(meta)]; .print("Robot_does_not_notice ..."); tofile("Robot_does_not_notice"); !robot_leaves.
+!dropped : robot_notices <- -meta[source(meta)]; .print("robot is moving"); tofile("robot_noticed"); !checking_Distance.

+!checking_Distance : close <- -meta[source(meta)]; tofile("robot_close"); !robot_pick_up.
+!checking_Distance : far <- -meta[source(meta)]; tofile("robot_far"); !robot_leaves.

+!robot_pick_up : decisive <- -meta[source(meta)]; tofile("robot_pick_up"); !countlegs.
+!robot_pick_up : indecisive <- -meta[source(meta)]; tofile("robot_indecisive"); !robot_leaves.

+!robot_leaves <- -meta[source(meta)];.print("robot_leaves"); tofile("robot_left_it").

+!countlegs : leg1 <- .print("leg1_completed"); -leg1[source(percept)].
+!countlegs : leg2 <- .print("leg2_completed"); -leg2[source(percept)].
+!countlegs : leg3 <- .print("leg3_completed"); -leg3[source(percept)].
+!countlegs : leg4 <- .print("leg4_completed"); -leg4[source(percept)].
