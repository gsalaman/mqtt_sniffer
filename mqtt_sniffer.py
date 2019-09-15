from Tkinter import *
import paho.mqtt.client as mqtt

class Sniffer():
  def __init__(self):
    self.window = Tk()
    self.window.title("MQTT Sniffer")
    self.create_widgets()
    self.client = mqtt.Client("Glenns_sniffer")
    self.client.on_message = on_message

  def connect(self):
    broker = self.entry_broker.get()
    print("connecting to "+broker)
    self.client.connect(self.entry_broker.get())
    print("...connected.")
    self.client.loop_start()
    #self.client.subscribe("#")
    
  def publish(self):
    topic = self.entry_topic.get()
    payload = self.entry_payload.get()
    print("publishing topic:   "+topic)
    print("           payload: "+payload)
    self.client.publish(topic, payload)

  def subscribe(self):
    topic = self.entry_subscribe_topic.get()
    print("subscribing to "+topic)
    self.client.subscribe(topic)

  def unsubscribe(self):
    topic = self.entry_subscribe_topic.get()
    print("unsubscribing to "+topic)
    self.client.unsubscribe(topic)

  def create_widgets(self):
    self.broker_frame = LabelFrame(self.window,text="Broker")
    self.label_broker = Label(self.broker_frame,text="hostname or address")
    self.label_broker.grid(row=0,column=0)
    self.entry_broker = Entry(self.broker_frame)
    self.entry_broker.grid(row=0,column=1)
    self.button_broker = Button(self.broker_frame, 
                                text="Connect",
                                command=self.connect)
    self.button_broker.grid(row=0,column=2)
    self.broker_frame.grid(row=0,column=0)

    self.publish_frame = LabelFrame(self.window,text="Publisher")
    self.label_topic = Label(self.publish_frame,text="Topic:")
    self.label_topic.grid(row=0,column=0)
    self.entry_topic = Entry(self.publish_frame)
    self.entry_topic.grid(row=0,column=1)
    self.label_payload = Label(self.publish_frame, text="Payload:")
    self.label_payload.grid(row=1,column=0)
    self.entry_payload = Entry(self.publish_frame)
    self.entry_payload.grid(row=1,column=1)
    self.button_publish = Button(self.publish_frame,
                                 text="Publish Message",
                                 command=self.publish)
    self.button_publish.grid(row=2,column=1)
    self.publish_frame.grid(row=1,column=0)

    self.subscribe_frame = LabelFrame(self.window,text="Subscriber")
    self.label_subscribe_topic = Label(self.subscribe_frame,text="Topic:")
    self.label_subscribe_topic.grid(row=0,column=0)
    self.entry_subscribe_topic = Entry(self.subscribe_frame)
    self.entry_subscribe_topic.grid(row=0,column=1)
    self.button_subscribe = Button(self.subscribe_frame, 
                                   text="Subscribe",
                                   command=self.subscribe)
    self.button_subscribe.grid(row=1,column=0)
    self.button_unsubscribe = Button(self.subscribe_frame,
                                     text="Unsubscribe",
                                     command=self.unsubscribe)
    self.button_unsubscribe.grid(row=1,column=1)
    self.subscribe_frame.grid(row=2,column=0)

#####################################################
# Message callback for MQTT
#####################################################
def on_message(client, userdata, message):
  #print "CALLBACK"

  print("Message topic: "+message.topic+" Message payload: "+message.payload)

######################################################
# Main
######################################################
my_window = Sniffer()
my_window.window.mainloop()

