public class UnitConverter {
 public static void main(String[] args) {
  if(args.length<3){System.out.println("Usage: java UnitConverter <value> <km|mi|c|f> <km|mi|c|f>");return;}
  double v=Double.parseDouble(args[0]); String from=args[1],to=args[2]; double out;
  if(from.equals("km")&&to.equals("mi")) out=v*0.621371;
  else if(from.equals("mi")&&to.equals("km")) out=v/0.621371;
  else if(from.equals("c")&&to.equals("f")) out=v*9/5+32;
  else if(from.equals("f")&&to.equals("c")) out=(v-32)*5/9;
  else {System.out.println("Unsupported conversion");return;}
  System.out.printf("%.2f %s = %.2f %s%n",v,from,out,to);
 }
}
