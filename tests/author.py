from tests.config import async_call


extrinsic = '0x0123456789'

commands = [("author_submitExtrinsic", [extrinsic]),  # bytes
            ("author_pendingExtrinsics", []),  # no para
            ("author_removeExtrinsic", [extrinsic])  # bytes_or_hash
            ]


for command, parameter in commands:
    async_call(command, [extrinsic])


# [pubsub(subscription = "author_extrinsicUpdate", subscribe, name = "author_submitAndWatchExtrinsic")]
# watch_extrinsic( & self, metadata: Self::Metadata, subscriber: Subscriber < Status < Hash, BlockHash >>, bytes: Bytes);
# [pubsub(subscription = "author_extrinsicUpdate", unsubscribe, name = "author_unwatchExtrinsic")]
# unwatch_extrinsic( & self, metadata: Option < Self::Metadata >, id: SubscriptionId) -> Result < bool >;


