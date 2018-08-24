// Agent robot in project Reactive_BDI_Env.mas2j

/* Initial beliefs and rules */

/* Initial goals */

!setup.
/* Plans */

+!setup : meta <- .print("Human is activated"); !activate.
+!setup : true <- !setup.

+!activate : leg1 <- -meta[source(meta)];.print("Leg please"); tofile("inform_leg_begin"); tofile("React"); coverage("plan1"); !informed.
+!activate : leg2 <- -meta[source(meta)];.print("Leg please"); tofile("inform_leg_begin"); tofile("React"); coverage("plan2"); !informed.
+!activate : leg3 <- -meta[source(meta)];.print("Leg please"); tofile("inform_leg_begin"); tofile("React"); coverage("plan3"); !informed.
+!activate : leg4 <- -meta[source(meta)];.print("Leg please"); tofile("inform_leg_begin"); tofile("React"); coverage("plan4"); !informed.


+!informed : dropped & leg1 <- -meta[source(meta)]; .print("leg1 Dropped"); tofile("Leg_Dropped");  coverage("plan49"); !dropped.
+!informed : dropped & leg2 <- -meta[source(meta)]; .print("leg2 Dropped"); tofile("Leg_Dropped");  coverage("plan50");!dropped.
+!informed : dropped & leg3 <- -meta[source(meta)]; .print("leg3 Dropped"); tofile("Leg_Dropped");  coverage("plan51");!dropped.
+!informed : dropped & leg4 <- -meta[source(meta)]; .print("leg4 Dropped"); tofile("Leg_Dropped");  coverage("plan52");!dropped.

+!dropped : human_notices <- -meta[source(meta)]; .print("human_notices"); tofile("human_notices"); coverage("plan53"); !checking_Distance.
+!dropped : human_waits <--meta[source(meta)]; .print("Waiting ..."); tofile("human_waits"); coverage("plan54");  !human_leaves.


+!checking_Distance : close <- -meta[source(meta)]; tofile("human_close"); coverage("plan55"); !human_pick_up.
+!checking_Distance : far <- -meta[source(meta)]; tofile("human_far"); coverage("plan56"); !human_leaves.

+!human_pick_up : decisive <- .print("human_picks_up"); -meta[source(meta)]; tofile("human_pick_up"); coverage("plan57"); coverage("plan60"); !countlegs.
+!human_pick_up : indecisive <- .print("human_leaves"); -meta[source(meta)]; tofile("human_indecisive"); coverage("plan58"); !human_leaves.

+!human_leaves <- -meta[source(meta)];.print("human_leaves"); tofile("human_left_it") coverage("plan59"); !countlegs.
 
+!countlegs : leg1 <-  -leg1[source(percept)]; coverage("plan45"); tofile("----------").
+!countlegs : leg2 <-  -leg2[source(percept)]; coverage("plan46"); tofile("----------").
+!countlegs : leg3 <-  -leg3[source(percept)]; coverage("plan47"); tofile("----------").
+!countlegs : leg4 <-  -leg4[source(percept)]; coverage("plan48"); tofile("----------").

