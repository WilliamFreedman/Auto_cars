import java.util.HashSet;

public class Lamp extends Position{

    private int ID;

    private int r;

    private HashSet<Car> cars;

    public Lamp()
    {
        position = new Vector2(0,0);
    }

    public int getID()
    {
        return ID;
    }

    public int getR()
    {
        return r;
    }

    public void setR(int r)
    {
        this.r = r;
    }
    public String toString()
    {
        return String.valueOf(ID);
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
