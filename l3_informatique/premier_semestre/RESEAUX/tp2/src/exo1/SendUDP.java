package exo1;
import java.io.IOException;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;
import java.net.UnknownHostException;

public class SendUDP {
	public static void main(String[] args) {
		int port = Integer.parseInt(args[0]);
		DatagramSocket datagramSocket;

		InetAddress ipAddr;
		try {
			ipAddr = InetAddress.getByName(args[1]);
			datagramSocket = new DatagramSocket();
			byte[] buffer = "Hello World".getBytes();
			DatagramPacket packet = new DatagramPacket(buffer, buffer.length, ipAddr, 4444);
			
			datagramSocket.send(packet);
			datagramSocket.close();


		} catch (IOException e) {
			e.printStackTrace();
		}



	}
}
