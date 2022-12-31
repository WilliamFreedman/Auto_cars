import java.util.HashMap;

public class Lamp {

    private int ID;

    private Vector2 position;

    private HashMap<Integer,Car> cars;

    public Vector2 getPosition()
    {
        return position;
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
