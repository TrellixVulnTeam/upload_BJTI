/**
 * Created by Fabian on 2017-03-24.
 */db.createUser(
    {
        user:"fabian",
        pwd:"fabian",
        roles: [{role:"dbOwner", db: "thedb"}]

    }
)