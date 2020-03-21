from warrant import Cognito

u = Cognito(
  user_pool_id ='eu-central-1_uP7h7e0Mn',  #user-pool-id
  client_id= '2ps7fiba6pudriblsanse371mk', #app-client-id
  client_secret='1qhru4qnh1uqmem5thqsol3n9fc75afnbnnkmmcdcreeffulv6ql',
  user_pool_region='eu-central-1',
  username='testpatient',
)

u.authenticate(password='Testpatient1!')