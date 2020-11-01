import java.net.URL;
import java.net.HttpURLConnection;
import java.util.Scanner;
import java.io.OutputStream;
import java.io.BufferedReader;
import java.io.InputStreamReader;

public class URLopenConnectionExample1{

public static void main(String args[]) throws Exception{  
  URL url = new URL("https://localhost:45783/myapi/coupons");
  HttpURLConnection connection = (HttpURLConnection)url.openConnection( );
  connection.setRequestMethod("POST");
  connection.setRequestProperty("Content-Type", "application/json; utf-8");
  connection.setRequestProperty("Accept", "application/json");
  connection.setDoOutput(true);
  String jsonInputString = ("{\"couponTest\":\"14000\"}");
  try(OutputStream os = connection.getOutputStream()) {
    byte[] input = jsonInputString.getBytes("utf-8");
    os.write(input, 0, input.length);
  }

  try(BufferedReader br = new BufferedReader(new InputStreamReader(connection.getInputStream(), "utf-8"))) {
    StringBuilder response = new StringBuilder();
    String responseLine = null;
    while ((responseLine = br.readLine()) != null) {
      response.append(responseLine.trim());
    }
  
    System.out.println(response.toString());
    }
  }
}
