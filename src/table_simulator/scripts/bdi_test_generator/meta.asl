// Created by Harrison Boyns 2018 //

// Script that delivers the meta beliefs from the drop_loop_run.py script to the ASLP agents //

// Agent meta in project BDI_TEST_GEN_2.mas2j

/* Initial beliefs and rules */

/* Initial goals */


!setup.

/* Plans */

+!setup : true <- get_beliefs; .print("hello world. This is the meta speaking"); .send(human, tell, meta).


