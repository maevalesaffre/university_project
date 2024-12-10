package exercice2;

import java.net.*;

public class ReceiveMulticast {
	public static void main(String args[]) {
		MulticastSocket s = null;
		try {
			int port = Integer.parseInt(args[0]);
			InetAddress ipAddress = InetAddress.getByName(args[1]);
			InetSocketAddress group = new InetSocketAddress(ipAddress,port);
			s = new MulticastSocket(port);
			NetworkInterface netInf = NetworkInterface.getByName("eth0");
			byte[] buff = new byte[1024];
			s.joinGroup(new InetSocketAddress(ipAddress,0), netInf);
			DatagramPacket p = new DatagramPacket(buff, buff.length, group);
			while (true ) {
				s.receive(p);
				System.out.println(
						"paquet reçu de : " + p.getAddress() + "\nport : " + p.getPort() + "\ntaille : " + p.getLength());
				System.out.println("message : " + new String(p.getData()) + "\n");
			}
		} catch (Exception e) {
			e.printStackTrace();
		} finally {
			s.close();							
		}
	}
}
