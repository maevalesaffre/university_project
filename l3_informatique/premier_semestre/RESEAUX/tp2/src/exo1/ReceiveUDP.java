package exo1;
import java.io.IOException;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;
import java.net.SocketException;
import java.net.UnknownHostException;

public class ReceiveUDP {

	public static void main(String[] args) {
		int port = Integer.parseInt(args[0]);
		DatagramSocket datagramSocket;
		
		
		try {
			InetAddress ipAddr = InetAddress.getByName("localhost");
			datagramSocket = new DatagramSocket(port, ipAddr);
			byte[] buffer = new byte[128];
			DatagramPacket packet = new DatagramPacket(buffer, buffer.length);
			while(true) {
				datagramSocket.receive(packet);
				System.out.println(new String(packet.getData(), "UTF-8"));
			}
			
		} catch (IOException e) {
			e.printStackTrace();
		}
		
		
	}
}
