package exercice2;

import java.net.DatagramPacket;
import java.net.InetAddress;
import java.net.MulticastSocket;
import java.net.NetworkInterface;
import java.net.InetSocketAddress;

public class SendMulticast {
	public static void main(String[] args) {
		MulticastSocket s = null;
		try {
			int dstPort = Integer.parseInt(args[0]);
			InetAddress dst = InetAddress.getByName(args[1]);
			InetSocketAddress group = new InetSocketAddress(dst,dstPort);
			s = new MulticastSocket(dstPort);
			NetworkInterface netInf = NetworkInterface.getByName("eth0");
			String message = args[2];
			byte[] buffer = message.getBytes();
			s.joinGroup(new InetSocketAddress(dst,0) ,netInf);
			DatagramPacket p = new DatagramPacket(buffer, buffer.length, group);



			s.send(p);
		} catch (Exception e) {
			e.printStackTrace();
		} finally {
			s.close();
		}
	}
}