import etcd3gw
import pytest

def test_etcd_operations():
    """Tests basic etcd operations."""
    client = etcd3gw.client(host='etcd1', port=2379)

    # Put a key
    client.put('mykey', 'myvalue')

    # Get the key
    value, *_ = client.get('mykey')
    assert value == b'myvalue'

    # Delete the key
    client.delete('mykey')

    # Get the key again
    result = client.get('mykey')
    assert result == []
