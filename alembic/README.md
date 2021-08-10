### Applying migrations
Generated migrations are usually located in the "alembic / versions" directory
For migrations to take effect, use the command:
```shell
$ alembic upgrade head
```
> Make sure that during the migration you have an active virtual environment in which Almbic is already installed!

> Before applying migrations, it is necessary to load variables carrying information about the Database into the environment.
> The variables required for the migrations to work can be found in the `assets/envs/template template`.

### Creating a revision
The creation of a new revision involves the introduction of significant (meaningful)
changes to the structure of the Database.

Before applying migrations, you should make sure that you have made 
independent changes to the structure of the Database in the `schema/meta.py` file

```shell
$ alembic revision -m "<Some comment about yours migration>" --autogenerate
```

After executing the command, a new migration file will appear in the `alembic/versions` folder. The file should be examined 
and the system-generated "plugs" comments should be removed.

> Don't forget to add the generated migration file to source control!
> ```shell
> $ git add alembic/versions
> ```