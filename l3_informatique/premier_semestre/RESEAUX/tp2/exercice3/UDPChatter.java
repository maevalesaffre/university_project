package exercice3;

import java.io.IOException;
import java.net.InetAddress;
import java.net.UnknownHostException;
import java.net.InetSocketAddress;
import java.net.NetworkInterface;
import java.net.SocketException;
import java.net.MulticastSocket;
import java.net.DatagramPacket;


public class UDPChatter {
    protected String userName;
    protected int p;
    protected MulticastSocket socket;
    protected String face;
    protected String inetAddr;

    public UDPChatter(String userName,String inetAddr, String face, int p) {
        this.userName = userName;
        this.inetAddr = inetAddr;
        this.p = p;
        this.face = face;
        
        try {
            InetAddress mCastAddr = InetAddress.getByName(this.inetAddr);
            InetSocketAddress group = new InetSocketAddress(mCastAddr, 0);
            NetworkInterface netIf = NetworkInterface.getByName(this.face);
            this.socket = new MulticastSocket(this.p);
            this.socket.joinGroup(group, netIf);
        } catch (IOException e) {
            e.printStackTrace();
        }

    }

    public void sendMessage(String msg) throws UnknownHostException {
        String sMessage = userName+": "+msg+"\n";
        DatagramPacket packet = new DatagramPacket(sMessage.getBytes(), sMessage.length(), InetAddress.getByName(this.inetAddr) , this.port);
        try {
            socket.send(packet);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public void receiveMessage(){
        byte[] buffer = new byte[130];
        DatagramPacket packet = new DatagramPacket(buffer, buffer.length);
        try {
            while(true) {
                socket.receive(packet);
                String recvMsg = new String(packet.getData(), "UTF-8");
                if (!recvMsg.startsWith(this.userName)) {
                	System.out.println(recvMsg);
                }
                
            }
           
            
        } catch (IOException e) {
            if(socket.isClosed()) {
            	System.out.println("the socket Closed");
            }
        }
    }
}
