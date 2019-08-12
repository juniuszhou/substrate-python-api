#
# class SystemInfo:
#      chainId
#      chainName
#      version
#      tokenDecimals
#      tokenSymbol
#
#
# class SystemHealth:
#      peers
#      isSyncing
#      shouldHavePeers
#
#
# class PeerInfo:
#      bestHash
#       bestNumber
#      peerId
#       protocolVersion
#      roles
#
#
# class PeersInfo:
#      count
#     PeerInfo peers
#
#
# class Endpo:
#      dialing
#
#
# class ConnectedPeerTime:
#       nanos
#       secs
#
#
# class ConnectedPeerInfo:
#      enabled
#     Endpo endpo
#      knownAddresses
#     ConnectedPeerTime latestPingTime
#      open
#      versionString
#
#
# class NotConnectedPeerInfo:
#      knownAddresses
#
#
# class ConnectedPeer:
#      key
#     ConnectedPeerInfo connectedPeerInfo
#
#
# class NotConnectedPeer:
#      key
#     NotConnectedPeerInfo notConnectedPeerInfo
#
#
# class NetworkState:
#       AverageDownloadPerSec
#       AverageUploadPerSec
#     ConnectedPeer connectedPeers
#      externalAddresses
#      listenedAddresses
#     NotConnectedPeer notConnectedPeers
#      peerId
#      peerset
