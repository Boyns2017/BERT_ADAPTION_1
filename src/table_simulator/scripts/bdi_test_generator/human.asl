// Agent robot in project Reactive_BDI_Env.mas2j

/* Initial beliefs and rules */

/* Initial goals */

!setup.
/* Plans */

+!setup : meta <- .print("Human is activated"); !activate.
+!setup : true <- !setup.

+!activate : leg1 <- -meta[source(meta)]; .print("leg1 Dropped");  !dropped.
+!activate : leg2 <- -meta[source(meta)]; .print("leg1 Dropped");  !dropped.
+!activate : leg3 <- -meta[source(meta)]; .print("leg1 Dropped");  !dropped.
+!activate : leg4 <- -meta[source(meta)]; .print("leg1 Dropped"); !dropped.

+!dropped : human_noticed <- -meta[source(meta)]; .print("human_notices"); tofile("human_noticed"); !checking_Distance.
+!dropped : human_waits <--meta[source(meta)]; .print("Waiting ..."); tofile("human_waits"); !human_leaves.


+!checking_Distance : close <- -meta[source(meta)]; tofile("human_close"); !human_pick_up.
+!checking_Distance : far <- -meta[source(meta)]; tofile("human_far"); !human_leaves.

+!human_pick_up : decisive <- .print("human_picks_up"); -meta[source(meta)]; tofile("human_pick_up"); !countlegs.
+!human_pick_up : indecisive <- .print("human_leaves"); -meta[source(meta)]; tofile("human_indecisive"); !human_leaves.

+!human_leaves <- -meta[source(meta)];.print("human_leaves"); tofile("human_left_it")!countlegs.

+!countlegs : leg1 <-  -leg1[source(percept)]; tofile("----------").
+!countlegs : leg2 <-  -leg2[source(percept)]; tofile("----------").
+!countlegs : leg3 <-  -leg3[source(percept)]; tofile("----------").
+!countlegs : leg4 <-  -leg4[source(percept)]; tofile("----------").

