import java.util.HashMap;
public class Car extends Position{

    private int ID;
    private Vector2 velocity;
    private Vector2 acceleration;
    private HashMap<Integer,Car> proximity;

    public Car()
    {
        position = new Vector2(0,0);
    }

    public String toString()
    {
        return String.valueOf(ID);
    }

    private Vector2 updatePosition(int x, int y)
    {
        position.update(x,y);
        return position;
    }

    private boolean equals(Car other)
    {
        return ID == other.ID;
    }

    public int getID()
    {
        return ID;
    }
    public int hashCode()
    {
        return Integer.hashCode(ID);
    }

    private Vector2 updateVelocity(int x, int y)
    {
        velocity.update(x,y);
        return velocity;
    }

    private Vector2 updateAcceleration(int x, int y)
    {
        acceleration.update(x,y);
        return acceleration;
    }

    public Vector2 getPosition()
    {
        return position;
    }

    public Vector2 getVelocity() {
        return velocity;
    }

    public Vector2 getAcceleration()
    {
        return acceleration;
    }

    public Packet passTime(int t)
    {
        Vector2 deltaX = velocity.mul(t).add(acceleration.mul(.5*Math.pow(t,2)));
        Vector2 deltaV = acceleration.mul(t);
        position.update(deltaX);
        velocity.update(deltaV);
        return generatePacket();
    }

    public Packet generatePacket()
    {
        return new Packet(ID,position,velocity,acceleration);
    }

    public void addNear(Car c)
    {
        proximity.put(c.ID,c);
    }

    public boolean isNear(Car c)
    {
        return proximity.containsKey(c.ID);
    }
    

}
