public class Packet {

    private final int ID;
    private final Vector2 pos;
    private final Vector2 vel;
    private final Vector2 acc;

    public Packet(int ID, Vector2 pos, Vector2 vel, Vector2 acc)
    {
        this.ID = ID;
        this.pos = pos;
        this.vel = vel;
        this.acc = acc;
    }

}