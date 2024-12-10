package exercice1;

import java.net.*;

public class SendUdp {
	
	public static void main(String[] args) {
		try {
			DatagramSocket s = new DatagramSocket();
			String message = args[2];
			InetAddress dst = InetAddress.getByName(args[1]);
			int dstPort = Integer.parseInt(args[0]);
			byte[] buffer = message.getBytes();
			DatagramPacket p = new DatagramPacket(buffer, buffer.length,dst, dstPort);
			s.send(p);
			s.close();
		} catch(Exception e) {
			e.printStackTrace();
		}
	}

}