# See discussion and more examples at http://packages.python.org/pymqi/examples.html
# or in doc/sphinx/examples.rst in the source distribution.

import pymqi

queue_manager = "QM01"
channel = "SVRCONN.1"
host = "192.168.1.135"
port = "1434"
queue_name = "TEST.1"
message = "Here's a reply"
conn_info = "%s(%s)" % (host, port)

qmgr = pymqi.connect(queue_manager, channel, conn_info)

md = pymqi.MD()

queue = pymqi.Queue(qmgr, queue_name)
message = queue.get(None, md)

reply_to_queue_name = md.ReplyToQ.strip()
reply_to_queue = pymqi.Queue(qmgr, reply_to_queue_name)
reply_to_queue.put(message)

queue.close()
qmgr.disconnect()
