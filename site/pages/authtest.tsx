import { withPageAuthRequired } from '@auth0/nextjs-auth0';

export default function Profile({ user }) {
  return <div>Hello {user.name}</div>;
}

export const getServerSideProps = withPageAuthRequired();