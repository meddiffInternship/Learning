
# coding: utf-8

# # basic tensorflow

# In[20]:

import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data


# In[8]:

#creating abstract tensor
x1 = tf.constant(5)
x2 = tf.constant(6)
res = tf.multiply(x1,x2)
print(res)


# In[14]:

''''
sess = tf.Session()
print(sess.run(res))
sess.close()
'''
with tf.Session() as sess:
    output = sess.run(res)
    print(output)
print(sess.run(res))


# # neural   network

# In[26]:

mnist = input_data.read_data_sets("home/aayushi/",one_hot = True)
nodes_h1 = 500
nodes_h2 = 500
nodes_h3 = 500
classes = 10
batch_size = 100
x = tf.placeholder('float',[None,784])
y = tf.placeholder('float')

def neural_nw(data):
    hidden_layer1 = {'weights':tf.Variable(tf.random_normal([784,nodes_h1])),
                    'biases':tf.Variable(tf.random_normal([nodes_h1]))}
    hidden_layer2 = {'weights':tf.Variable(tf.random_normal([nodes_h1,nodes_h2])),
                    'biases':tf.Variable(tf.random_normal([nodes_h2]))}
    hidden_layer3 = {'weights':tf.Variable(tf.random_normal([nodes_h2,nodes_h3])),
                    'biases':tf.Variable(tf.random_normal([nodes_h3]))}
    output_layer = {'weights':tf.Variable(tf.random_normal([nodes_h1,classes])),
                    'biases':tf.Variable(tf.random_normal([classes]))}
    
    l1 = tf.add(tf.multiply(data,hidden_layer1['weights']), hidden_layer1['biases'])
    l1 = tf.nn.relu(l1)
    l2 = tf.add(tf.multiply(l1,hidden_layer2['weights']) ,hidden_layer2['biases'])
    l2 = tf.nn.relu(l2)
    l3 = tf.add(tf.multiply(l2,hidden_layer3['weights']) ,hidden_layer3['biases'])
    l3 = tf.nn.relu(l3)
    op = tf.multiply(l3,output_layer1['weights'] + output_layer1['biases'])
    return output

def train_nw(x):
    prediction = neural_nw(x)
    cost = tf.reduce_mean(tf.nn.sigmoid_cross_entropy_with_logits(prediction,y))
    optimizer = tf.train.AdamOptimizer().minimize(cost)
    no_epochs = 5
    
    with tdf.Session() as sess:
        sess.run(tf.initialize_all_variables())
        for epoch in no_epochs:
            epoch_loss = 0
            for _ in(range(mnist.train.num_examples/batch_size)):
                epoch_x,epoch_y = mnist.train.next_batch(batch_size)
                _, c = sess.run([optimizer,cost], feed_dict = {x:epoch_x,y:epoch_y})
                epoch_loss+= c 
            print('Epoch',epoch,'completed out of',no_epochs,'loss',epoch_loss)
        correct = tf.equal(tf.argmax(prediction,1), tf.argmax(y,1))
        accuracy = tf.reduce_mean(tf.cast(correct,'float'))
        print('Accuracy:',accuracy.eval({x:mnist.test.images, y:mnist.test.labels}))

                

train_nw(x)
    

