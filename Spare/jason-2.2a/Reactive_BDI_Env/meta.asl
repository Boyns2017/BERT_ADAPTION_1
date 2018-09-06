// Agent meta in project Reactive_BDI_Env.mas2j

/* Initial beliefs and rules */

/* Initial goals */

!setup.

/* Plans */

+!setup : true <- get_beliefs; tofile("This worked somewhat"); .print("hello world. This is the meta speaking"); .send(human, tell, meta).

