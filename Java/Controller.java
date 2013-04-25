package Java;

import java.io.*;
import java.util.*;

public class Controller {
  private List<Population> deviations;
  private int reportIns;

  public class Population {
    public int size;
    public double std;
    public double mean;

    public Population(int size, double std, double mean) {
      this.size = size;
      this.std = std;
      this.mean = mean;
    }

    public Population combine(Population b) {
      Population a = this;
      int new_size = a.size + b.size;
      double weighted_variance = ((a.std * a.std * ((double)a.size)) + (b.std * b.std * ((double)b.size))) / ((double)new_size);
      double mean_variance = Math.pow(a.mean - b.mean, 2.0) * (((double)a.size) * ((double)b.size)) / Math.pow((double)new_size, 2.0);
      double new_std = Math.sqrt(weighted_variance + mean_variance);
      double new_mean = (((double)a.size) * a.mean + ((double)b.size) * b.mean) / ((double)new_size);
      return new Population(new_size, new_std, new_mean);
    }
  }

  public Controller() {
    deviations = new ArrayList<Population>();
    reportIns = 0;
  }

  private void finalMergeStds() {
    for (int i = 1; i < 100; i++) {
      deviations.get(0).combine(deviations.get(i));
    }
    System.out.println((int)deviations.get(0).std);
  }

  public synchronized void submitStats(double mean, double f) {
    deviations.add(new Population(100, f, mean));
    if (++reportIns >= 100) {
      finalMergeStds();
    }
  }

  public static void main(String[] args) throws IOException {
    Controller self = new Controller();
    Server.main(args);
    for (int i = 0; i < 100; i++) {
      Client c = new Client(self);
    }
  }
}
