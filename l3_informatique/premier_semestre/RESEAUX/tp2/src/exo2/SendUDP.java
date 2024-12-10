package exo2;
import java.io.IOException;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;
import java.net.InetSocketAddress;
import java.net.MulticastSocket;
import java.net.NetworkInterface;
import java.net.UnknownHostException;

public class SendUDP {
	public static void main(String[] args) {
		int port = Integer.parseInt("7654");
		MulticastSocket multicastSocket;

		try {
			InetAddress mCastAddr = InetAddress.getByName("224.0.0.1");
			InetSocketAddress group = new InetSocketAddress(mCastAddr, 0);
			NetworkInterface netIf = NetworkInterface.getByName("eth0");
			multicastSocket = new MulticastSocket();
			multicastSocket.joinGroup(group, netIf);
			byte[] buffer = "HELLO".getBytes();
			DatagramPacket packet = new DatagramPacket(buffer, buffer.length, mCastAddr, 7654);

			multicastSocket.send(packet);

		} catch (IOException e) {
			e.printStackTrace();
		}


	}
}
