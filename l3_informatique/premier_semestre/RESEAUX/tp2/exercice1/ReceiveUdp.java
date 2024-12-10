package exercice1;

import java.net.*;

public class ReceiveUdp {
	public static void main(String args[]) {
		
		try {
			InetAddress ipAddress = InetAddress.getByName(args[1]);
			byte[] octets = args[2].getBytes();
			DatagramSocket s = new DatagramSocket(Integer.parseInt(args[0]));
			DatagramPacket p = new DatagramPacket(octets, octets.length, ipAddress , Integer.parseInt(args[0]));
			s.receive(p);
			System.out.println("paquet reçu de : " + p.getAddress()+
								"\nport : " +           p.getPort()+
								"\ntaille : " +         p.getLength());
			System.out.println("message : "+ new String(p.getData()));
			s.close();
		}catch(Exception e) {
			e.printStackTrace();
		}
	}
}
