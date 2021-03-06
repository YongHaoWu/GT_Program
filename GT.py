
#!/usr/bin/env python
# -*- coding: utf-8 -*-

' a module to analyse socket'

__author__ = 'YongHao Hu'

import analyse_socket
import numpy as np
import analyse_packet

class Discriminators(object):
    def __init__(self, num_of_forward_message, num_of_backward_message,
                 size_of_forward_message, size_of_backward_message,
                 min_len_of_forward_message, min_len_of_backward_message,
                 avg_len_of_forward_message, avg_len_of_backward_message,
                 stand_deviation_len_of_forward_message, stand_deviation_of_backward_message,
                 min_arrive_timegap_of_forward_message, min_arrive_timegap_of_backward_message,
                 avg_arrive_timegap_of_forward_message, avg_arrive_timegap_of_backward_message,
                 max_arrive_timegap_of_forward_message, max_arrive_timegap_of_backward_message,
                 stand_deviation_arrive_timegap_of_forward_message, stand_deviation_arrive_timegap_of_backward_message,
                 num_of_urgent_forward_message, num_of_urgent_backward_message,
                 num_of_push_forward_message, num_of_push_backward_message,
                 time_duration_of_stream):
        pass

#mysockets = analyse_socket.analyse_lsof("lsof.txt")
print "main program \n"
#analyse_socket.print_sockets(mysockets[1])
#analyse_socket.print_sockets(mysockets[2])
#analyse_socket.print_sockets(mysockets[4])
#analyse_socket.print_sockets(mysockets[9])
mypackets = analyse_packet.analyse_tcpdump("new.txt")
print len(mypackets)
analyse_packet.print_packets(mypackets[0])
analyse_packet.print_packets(mypackets[1])
analyse_packet.print_packets(mypackets[len(mypackets)-1])
analyse_packet.print_packets(mypackets[len(mypackets)-2])

num_of_urgent_forward_message = num_of_urgent_backward_message = num_of_push_forward_message = num_of_push_backward_message = num_of_forward_message =  num_of_backward_message =  0
unknow = 0
all_packet_length = []
forward_msg_length = []
backward_msg_length = []
arrive_timegap_of_forward_message = []
arrive_timegap_of_backward_message = []
all_timestamp = []
for single_packet in mypackets:
    #print single_packet.packet_length
    all_timestamp.append(single_packet.time_stamp)
    all_packet_length.append(single_packet.packet_length)
    precision = 1e-6
    if mypackets.index(single_packet)+1 != len(mypackets):
        diff = abs(float(mypackets[mypackets.index(single_packet)+1].time_stamp) - float(single_packet.time_stamp))
        if diff < precision:
            print "less"
            print diff
            diff = 0
            print float(mypackets[mypackets.index(single_packet)].time_stamp)
            print float(mypackets[mypackets.index(single_packet)+1].time_stamp)
            print (mypackets[mypackets.index(single_packet)].time_stamp)
            print (mypackets[mypackets.index(single_packet)+1].time_stamp)

    if single_packet.is_forward_message == 1:
        arrive_timegap_of_forward_message.append(diff)
        forward_msg_length.append(single_packet.packet_length)
        num_of_forward_message = num_of_forward_message+1
        if single_packet.flag == 'P.':
            num_of_push_forward_message += 1
        print "forward ", single_packet.quintet.SrcIp, single_packet.quintet.SrcPort
        print "backward ", single_packet.quintet.DstIP, single_packet.quintet.DstPort, "\n"
    elif single_packet.is_forward_message == 0:
        arrive_timegap_of_backward_message.append(diff)
        backward_msg_length.append(single_packet.packet_length)
        num_of_backward_message = num_of_backward_message+1
        if single_packet.flag == 'P.':
            num_of_push_backward_message += 1
        print "forward ", single_packet.quintet.SrcIp, single_packet.quintet.SrcPort, "\n"
        print "backward ", single_packet.quintet.DstIP, single_packet.quintet.DstPort
    else:
        unknow = unknow + 1

print "\n\n\nnum_of_forward_message is ", num_of_forward_message
print "\nnum_of_backward_message is ", num_of_backward_message
print "unknow  is ", unknow
all_packet_length = [int(i) for i in all_packet_length]
print "\n\n\nsum_of_forward_message is ", num_of_forward_message
print "\nsum_of_backward_message is ", num_of_backward_message
print "unknow  is ", unknow

## Convert all strings in a list to int
#print "all_packet_length"
#all_packet_length = [int(i) for i in all_packet_length]
#print min(all_packet_length)
#print max(all_packet_length)
#print sum(all_packet_length)/len(all_packet_length)

print "forward_msg_length"
forward_msg_length = [int(i) for i in forward_msg_length]
print min(forward_msg_length)
print max(forward_msg_length)
print sum(forward_msg_length)
print sum(forward_msg_length)/len(forward_msg_length)
print "standard"
print np.std(forward_msg_length, axis=0)

print "backward_msg_length"
backward_msg_length = [int(i) for i in backward_msg_length]
print min(backward_msg_length)
print max(backward_msg_length)
print sum(backward_msg_length)
print sum(backward_msg_length)/len(backward_msg_length)
print np.std(backward_msg_length, axis=0)

print "num_of_push_forward_message"
print num_of_push_forward_message
print "num_of_push_backward_message"
print num_of_push_backward_message


print "arrive_timegap_of_forward_message"
print min(arrive_timegap_of_forward_message)
print max(arrive_timegap_of_forward_message)
print sum(arrive_timegap_of_forward_message)/len(arrive_timegap_of_forward_message)
print np.std(arrive_timegap_of_forward_message, axis=0)
print "arrive_timegap_of_backward_message"
print min(arrive_timegap_of_backward_message)
print max(arrive_timegap_of_backward_message)
print sum(arrive_timegap_of_backward_message)/len(arrive_timegap_of_backward_message)
print np.std(arrive_timegap_of_backward_message, axis=0)
print "time_duration_of_stream"
print min(all_timestamp)
print max(all_timestamp)
print float(max(all_timestamp)) - float(min(all_timestamp))

#for i in arrive_timegap_of_backward_message:
#    print i
