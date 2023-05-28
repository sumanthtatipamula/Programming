import { Container } from 'inversify';
import { Types } from './types';
import { UsersApiServiceImpl } from './UsersApiServiceImpl';

let container = new Container();
container
	.bind<UsersApiServiceImpl>(Types.UserApiService)
	.to(UsersApiServiceImpl);
export { container };
