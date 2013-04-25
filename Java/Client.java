package Java;

import java.io.*;
import java.util.*;
import java.net.*;

public class Client implements Runnable {
  private Controller c;
  public void run() {
    try {
      URL url = new URL("http://localhost:8080");
      HttpURLConnection connection = (HttpURLConnection)url.openConnection();
      connection.setRequestMethod("GET");
      Scanner scan = new Scanner(connection.getInputStream());
      List<Integer> ints = new ArrayList<Integer>();
      while (scan.hasNextInt()) {
        ints.add(scan.nextInt());
      }
      int sum = 0;
      for (int item:ints) {
        sum += item;
      }
      double mean = ((double)sum) / ((double)ints.size());
      double variance = 0f;
      for (int item:ints) {
        variance += Math.pow(((double)item) - mean, 2f);
      }
      double deviation = Math.sqrt(variance);
      c.submitStats(mean, deviation);
    }
    catch (Exception e) {
      System.out.println("Shucks" + e.getMessage());
    }
  }
  
  public Client(Controller c) {
    this.c = c;
    new Thread(this).start();
  }
}
