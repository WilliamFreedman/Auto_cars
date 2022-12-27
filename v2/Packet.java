public class Packet {

    private final int ID;
    private final Vector2 pos;
    private final Vector2 vel;
    private final Vector2 acc;

    private boolean equals(Car other)
    {
        return ID == other.getID();
    }

    public int hashCode()
    {
        return Integer.hashCode(ID);
    }

    public Packet(int ID, Vector2 pos, Vector2 vel, Vector2 acc)
    {
        this.ID = ID;
        this.pos = pos;
        this.vel = vel;
        this.acc = acc;
    }

}