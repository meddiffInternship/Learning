import tensorflow as tf

x1 = tf.constant(5)
x2 = tf.constant(6)

res = tf.multiply(x1,x2)

print(res)

#sess = tf.Session()

with tf.Session() as sess:
    print(sess.run(res))
