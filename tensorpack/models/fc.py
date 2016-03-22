#!/usr/bin/env python2
# -*- coding: UTF-8 -*-
# File: fc.py
# Author: Yuxin Wu <ppwwyyxx@gmail.com>

import tensorflow as tf
import math

from ._common import layer_register
from ..tfutils.symbolic_functions import *

__all__ = ['FullyConnected']

@layer_register(summary_activation=True)
def FullyConnected(x, out_dim,
                   W_init=None, b_init=None,
                   nl=tf.nn.relu, use_bias=True):
    x = batch_flatten(x)
    in_dim = x.get_shape().as_list()[1]

    if W_init is None:
        #W_init = tf.truncated_normal_initializer(stddev=1 / math.sqrt(float(in_dim)))
        W_init = tf.uniform_unit_scaling_initializer()
    if b_init is None:
        b_init = tf.constant_initializer()

    W = tf.get_variable('W', [in_dim, out_dim], initializer=W_init)
    if use_bias:
        b = tf.get_variable('b', [out_dim], initializer=b_init)
    prod = tf.nn.xw_plus_b(x, W, b) if use_bias else tf.matmul(x, W)
    return nl(prod, name='output')
