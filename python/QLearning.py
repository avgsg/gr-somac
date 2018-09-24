#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import logging

class QLearning:

	def __init__(self):
		self.q_table	= np.zeros((2, 2))
		self.discount   = 0.8
		self.learn_rate = 0.2
		self.reward     = 0.
		
	def decision(self, prot):
		self.state = prot
		
		if self.q_table[self.state, 0] == self.q_table[self.state, 1]:
			action = np.random.randint(2)
		else:
			action = np.argmax(self.q_table[self.state, :])
		
		self.action = action
		self.state_new = action
		
		return action
	
	def update_qtable(self, reward):
		self.q_table[self.state, self.action] = (1. - self.learn_rate) * self.q_table[self.state, self.action] + \
						self.learn_rate * (reward + self.discount * np.max(self.q_table[self.state_new, :]))
		
		return