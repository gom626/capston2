#from confluent_kafka import Consumer, KafkaError, TopicPartition
from confluent_kafka import *
#from kafka import KafkaConsumer
from confluent_kafka.admin import AdminClient

settings = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'mygroup',
    'client.id': 'client-1',
    'enable.auto.commit': True,
    'session.timeout.ms': 6000,
    #'on_commit': commit_completed,
    #'default.topic.config': {
    'auto.offset.reset': 'earliest'
    #}
}

c = Consumer(settings)
t = TopicPartition('mytopic2', 0, 0)
#c.subscribe(['mytopic'])

def on_assign (c2, ps):
    for p in ps:
        p.offset=-2
        print(p.topic)
    c2.assign(ps)  

#c.subscribe(['mytopic'], on_assign=on_assign)
low, high = c.get_watermark_offsets(t)
print(high)
#print(t)
c.assign([t])
i=0
while i<high:
    msg = c.poll(0.1)
    
    if msg is None:
        continue
        #break
    elif not msg.error():
        print('Received message: {0}'.format(msg.value()))
        i = i+1
        #print(msg.offset())
        print(i)
        #print(msg.topic())
        #print(123)
    elif msg.error().code() == KafkaError._PARTITION_EOF:
        print('End of partition reached {0}/{1}'
                .format(msg.topic(), msg.partition()))
    else:
        print('Error occured: {0}'.format(msg.error().str()))

print("end")
c.close()