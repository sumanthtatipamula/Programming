import { UsersApiServiceImpl } from './UsersApiServiceImpl';
import { container } from './inversify.config';
import { Types } from './types';
const service = container.get<UsersApiServiceImpl>(Types.UserApiService);
service
	.getUsers()
	.then((user) => console.log(user))
	.catch((err) => console.log(err));
