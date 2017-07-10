import tensorflow as tf
x1 = tf.constant(5)
x2 = tf.constant(6)
result1=x1*x2
result = tf.multiply(x1,x2)
#print(result)
#print(result1)

sess=tf.Session()
print(sess.run(result))
sess.close()
