// Agent meta in project BDI_TEST_GEN_2.mas2j

/* Initial beliefs and rules */

/* Initial goals */


!setup.

/* Plans */

+!setup : true <- get_beliefs; .print("hello world. This is the meta speaking"); tofile("Leg_Dropped"); .send(robot, tell, meta); .send(human, tell, meta).


