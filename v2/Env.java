import java.util.HashMap;
public class Env {

    private int height;
    private int width;

    private HashMap<Integer,Car> cars;

    private HashMap<Integer,Lamp> lamps;

    public HashMap<Integer,Car> getCars()
    {
        return cars;
    }

    public HashMap<Integer,Lamp> getLamps()
    {
        return lamps;
    }

    public int getHeight()
    {
        return height;
    }

    public int getWidth()
    {
        return width;
    }

    public boolean pointWithin(Vector2 p)
    {
        if (p.getX()>width || p.getY() > height || p.getX()<=0 || p.getY() <=0)
        {
            return false;
        }

        return true;
    }

    public void newCar(Car c)
    {
        cars.put(c.getID(),c);
    }

    public void newLamp(Lamp l)
    {
        lamps.put(l.getID(),l);
    }



}
