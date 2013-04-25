package Java;

import java.io.*;
import java.util.*;
import java.net.*;
import java.nio.charset.Charset;
import com.sun.net.httpserver.*;

public class Server implements HttpHandler {
  private Scanner input;
  private int fNum;
  private HttpServer server;

  public Server(HttpServer server) {
    fNum = 1;
    this.server = server;
  }

  public void handle(HttpExchange exchange) throws IOException {
    String fname = String.format("%s/Setup/Files/%d", System.getProperty("user.dir"), fNum++);
    try {
      input = new Scanner(new FileReader(fname));
    }
    catch (FileNotFoundException e) {
      System.err.println(String.format("Couldn't find file: %s", fname));
      System.exit(1);
    }
    Headers responseHeaders = exchange.getResponseHeaders();
    responseHeaders.set("Content-Type", "text/plain");
    exchange.sendResponseHeaders(200, 0);
    OutputStream os = exchange.getResponseBody();
    while (input.hasNext()) {
      os.write((input.next() + "\n").getBytes(Charset.forName("UTF-8")));
    }
    input.close();
    os.close();
    if (fNum == 101) {
      server.stop(2);
    }
  }

  public static void main(String[] args) throws IOException {
    InetSocketAddress addr = new InetSocketAddress(8080);
    HttpServer server = HttpServer.create(addr, 0);

    server.createContext("/", new Server(server));
    server.setExecutor(null);
    server.start();
  }
}
