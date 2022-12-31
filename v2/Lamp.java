import java.util.HashMap;

public class Lamp extends Position{

    private int ID;


    private HashMap<Integer,Car> cars;

    public Lamp()
    {
        position = new Vector2(0,0);
    }
    public Vector2 distance(Lamp l)
    {
        return position.sub(l.getPosition());
    }

    public Vector2 distance(Car c)
    {
        return position.sub(c.getPosition());
    }



}
