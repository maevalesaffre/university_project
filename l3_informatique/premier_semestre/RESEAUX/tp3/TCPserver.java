package main;

import java.io.DataInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.io.PrintWriter;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.ArrayList;

public class TCPserver{

	static ArrayList<Socket> socketList = new ArrayList<Socket>();
	public static void main(String[] args) {
		try {
			ServerSocket serverSocket = new ServerSocket(2022);

			while (true) {
				Socket socket = serverSocket.accept();
				Thread t = new Thread( () -> {
					try {
						socketList.add(socket);
						OutputStream output;
						output = socket.getOutputStream();
						PrintWriter writer = new PrintWriter(output, true);
						writer.println("Bienvenue sur le serveur");

						InputStream input = socket.getInputStream();
						DataInputStream dis = new DataInputStream(input);

						byte buffer[] = new byte[1024];

						while(true) {
							if (dis.read(buffer) == -1) {
								return;
							} 
							for(Socket s: socketList) {
								OutputStream outputSocket;
								outputSocket = s.getOutputStream();
								PrintWriter socketWriter = new PrintWriter(outputSocket, true);
								socketWriter.println(new String(buffer, "UTF-8"));
							}

						}
					} catch (IOException e) {
						e.printStackTrace();
					}
				});
				t.start();
			}
		} catch (IOException e) {

			e.printStackTrace();
		}
	}


}
