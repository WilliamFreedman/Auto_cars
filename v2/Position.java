public abstract class Position {

    public Vector2 position;
    public Vector2 getPosition()
    {
        return position;
    }



    public Vector2 distance(Position p)
    {
       return position.sub(p.getPosition());
    }
}
