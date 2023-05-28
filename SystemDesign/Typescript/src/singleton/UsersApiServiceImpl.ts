import { injectable } from 'inversify';
import 'reflect-metadata';
import { UsersApiService } from './interface';

@injectable()
export class UsersApiServiceImpl implements UsersApiService {
	getUsers(): Promise<string[]> {
		return Promise.resolve(['Alex', 'John', 'Sarah']);
	}
}
