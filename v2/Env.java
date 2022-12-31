import java.util.HashMap;
public class Env {

    private int height;
    private int width;

    private HashMap<Integer,Car> cars;

    public HashMap<Integer,Car> getCars()
    {
        return cars;
    }

    public int getHeight()
    {
        return height;
    }

    public int getWidth()
    {
        return width;
    }


    public void newCar(Car c)
    {
        cars.put(c.getID(),c);
    }



}
