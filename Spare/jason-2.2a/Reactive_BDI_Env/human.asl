// Agent robot in project Reactive_BDI_Env.mas2j

/* Initial beliefs and rules */

/* Initial goals */

!setup.
/* Plans */

+!setup : meta <- !activate.
+!setup : true <- !setup.


+!activate <- .print("leg1 Dropped"); tofile("This worked somewhat"); !dropped.
+!activate : leg2 <- .print("leg2 Dropped"); !dropped.
+!activate : leg3 <- .print("leg3 Dropped"); !dropped.
+!activate : leg4 <- .print("leg4 Dropped"); !dropped.

+!dropped <-.print("human is moving"); !checking_Distance.

+!checking_Distance <- .print("Close"); !human_pick_up.
+!checking_Distance <- .print("Far"); !human_leaves.

+!human_pick_up <- .print("Picking Up"); !countlegs.
+!human_leaves <- .print("Leaving...."); !countlegs.


+!countlegs <- .print("Leg number 2"); +leg2; !activate.
+!countlegs <- .print("Leg number 3"); +leg3; !activate.
+!countlegs <- .print("Leg number 4"); +leg4; !activate.
