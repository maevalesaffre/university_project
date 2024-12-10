package exercice3;

import java.net.SocketException;
import java.net.UnknownHostException;
import java.util.Scanner;

public class UDPChat {
    public static void main(String[] args) {
        UDPChatter user = new UDPChatter(args[0],"224.0.0.1", "eth0", 7654);
        Scanner input = new Scanner(System.in);
        String msg;

        Thread thread = new Thread(() -> {
                user.receiveMessage();
            
        });
        thread.start();
        
        msg = input.next();
        while (msg.compareTo("exit") != 0){
            
            try {
                user.sendMessage(msg);
                msg = input.next();
            } catch (UnknownHostException e) {
                e.printStackTrace();
            }
        }
        user.socket.close();
        return;





    }
}
